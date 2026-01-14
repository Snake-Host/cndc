# Cloud Native Data Center (CNDC)

The Cloud Native Data Center (CNDC) is an open-source project that aims to create, deploy and automate a state-of-the-art data center architecture inspired by the best practices of the most referenced cloud environment giants. Its main approach relies on open-source technologies to make it both accessible and fully reproducible.

This project serves as a reliable source for cloud enthusiasts, system engineers, and developers who seek to explore and deploy a modular and automated cloud infrastructure.

CNDC is designed not only for the previous matter but also to dive in a learning journey that helps tackle cloud-native concepts even for beginners, and for advanced skills building, including customizing automation scripts, applying and implementing security best practices, and mostly contributing to the project.

# Project Structure

1. Introduction
   - Overview
   - Intended Audience
   - Prerequisites
   - Working Environment
   - Design Goals & Non-Goals

2. Networking – VXLAN-EVPN Fabric
   1. Overview
   2. Architecture & Design Decisions
   3. Deployment on Cisco Nexus 9000
      - Manual Configuration
      - Automated Deployment
   4. Deployment on SONiC NOS (Planned for a future release)
      - Manual Configuration
      - Automated Deployment

3. Platform (Compute & Storage)
   1. Proxmox Cluster (QEMU/KVM)
      - Overview
      - Manual Corosync Deployment (GUI)
      - Manual Ceph Deployment (GUI)
   2. Kubernetes/Ceph Cluster
      - Overview
      - Architecture & Networking Model
      - Kubernetes cluster bootstraping (Manual & Automated)
      - Ceph cluster bootstraping (Manual & Automated)
      - Kubernetes Storage Rook (Planned for a future release)
   3. Multi-cluster Kubernetes (Planned for a future release)

4. Operations & Day-2 (Planned for a future release)
   - Monitoring & Observability
   - Upgrades & Lifecycle
   - Failure Scenarios
   - Backup & Recovery

# License

This project is licensed under the GNU Affero General Public License v3.0 (AGPLv3).

If you want to use this software in a proprietary product, SaaS, or commercial
environment without the obligations of AGPLv3, a commercial license is available.

Contact: contact@zerith.cloud
